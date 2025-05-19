import sys
import os

# Add the parent directory (project root) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import plotly.express as px
import streamlit as st
from streamlit_searchbox import st_searchbox
from backend.crud import *
from datetime import date

st.set_page_config(page_title="Liana's Literary Lounge", layout="centered")
st.title("📚 Liana's Literary Lounge")

# Sidebar navigation
menu = st.sidebar.selectbox("Navigate", [
    "Show Books", "Add New Book", "Add New Borrower", "Lend Book", "Return Book", "STATS"
])

# Show books
if menu == "Show Books":
    st.header("Books Table")
    books_df = get_all_books_status()

    if books_df.empty:
        st.info("No books in the library yet.")
    else:
        styled_df = style_book_status(books_df)
        st.write("Legend: 🟢 Available | 🔴 Borrowed")
        st.write(styled_df.to_html(escape=False), unsafe_allow_html=True)

# Add new book
if menu == "Add New Book":
    st.header("📘 Add New Book to Liana’s Library")
    title = st.text_input("Book Title")
    language = st.text_input("Language")
    author_name = st.text_input("Author Full Name")
    genre_name = st.text_input("Genre Name")

    if st.button("Add Book"):
        result = call_add_new_book(title, author_name, genre_name, language)
        if result is True:
            st.success("Book added successfully!")
        else:
            st.error(result)

# Add new borrower
if menu == "Add New Borrower":
    st.header("👤 Add New Borrower to Liana’s Library")

    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    phone = st.text_input("Phone Number")
    email = st.text_input("Email Address")

    if st.button("Add Borrower"):
        result = call_add_new_borrower(fname, lname, phone, email)
        if result is True:
            st.success("Borrower added successfully!")
        else:
            st.error(result)

# Lend a book
if menu == "Lend Book":
    st.header("📕 Lend a Book")

    borrower = st_searchbox(search_borrowers, key="search_borrower", placeholder="Search borrower by name")
    book = st_searchbox(search_books, key="search_book", placeholder="Search book by title")
    date_borrowed = st.date_input("Date of Borrowing", date.today())

    if st.button("Confirm Loan"):
        if not borrower or not book:
            st.warning("Please select both a borrower and a book.")
        else:
            success, message = add_new_loan(borrower_id=borrower["id"], book_id=book["id"], date_of_borrowing=date_borrowed)
            if success:
                st.success(message)
            else:
                st.error(f"Loan failed: {message}")

# Return a book
if menu == "Return Book":
    st.header("📥 Return a Book")

    selected_book = st_searchbox(search_borrowed_books, key="return_book", placeholder="Search borrowed book")
    return_date = st.date_input("Return Date", date.today())

    if st.button("Confirm Return"):
        if not selected_book:
            st.warning("Please select a borrowed book to return.")
        else:
            success, msg = return_book(selected_book["id"], return_date)
            if success:
                st.success(msg)
            else:
                st.error(f"Return failed: {msg}")

# Get statistics

# Stats
if menu == "STATS":
    st.header("📊 Library Statistics")

    # Display general statistics
    stats = get_library_stats()

    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="👥 Total Borrowers", value=stats["total_borrowers"])
        st.metric(label="📚 Total Books", value=stats["total_books"])

    with col2:
        st.metric(label="🟢 Active Borrowers", value=stats["active_borrowers"])
        st.metric(label="📕 Books on Loan", value=stats["borrowed_books"])

    # Display pie chart for book status
    stats = get_book_loan_stats()
    fig = px.pie(
        names=list(stats.keys()),
        values=list(stats.values()),
        title="Library Book Status",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    st.plotly_chart(fig, use_container_width=True)

    # Display top borrowers
    top_borrowers_df = get_top_borrowers()

    st.subheader("🏆 Top 10 Borrowers by Number of Borrowed Books")
    if top_borrowers_df.empty:
        st.info("No active loans found.")
    else:
        fig1 = px.bar(top_borrowers_df, x="borrower", y="books_on_loan", color="books_on_loan",
                    labels={"books_on_loan": "Books on Loan"}, title="Top Borrowers",
                    color_continuous_scale='Blues')
        
    st.plotly_chart(fig1)