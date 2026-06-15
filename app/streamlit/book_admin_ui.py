import streamlit as st
import requests

# --- Configuration ---
# Replace this with the actual URL of your REST API endpoint
API_URL = "http://localhost:9999/add_book" 

def main():
    st.set_page_config(page_title="Book Management System", page_icon="📚")
    st.title("📚 Book Entry Form")
    st.write("Fill out the details below to add a new book to the database.")

    # Create a form to group the inputs together
    with st.form("book_form"):
        # Input fields
        book_id = st.text_input("Book Id", placeholder="Enter the Book Id like : B101")
        book_title = st.text_input("Book Title", placeholder="Enter the book title like : Sprint in Action")
        price = st.number_input("Price ($)", min_value=0.0, format="%.2f")
        count = st.number_input("Count", min_value=0, step=1)           
            
        # Submit button for the form
        submitted = st.form_submit_button("Submit Book Details")

    # Handle the form submission outside the form layout
    if submitted:
        # Basic validation to ensure required fields aren't empty
        if not book_id or not book_title or not price or not count:
            st.warning("Please fill in all four mandatory fields : Book ID, Book Title, Price and Count.")
        else:
            # Prepare the JSON payload
            payload = {
                "book_id": book_id,
                "book_title": book_title,
                "price": price,
                "count": count
            }
            
            # Call the REST API
            with st.spinner("Submitting Book Detail..."):
                try:
                    response = requests.post(API_URL, json=payload)
                    
                    # Check if the request was successful (200 OK or 201 Created)
                    if response.status_code in (200, 201):
                        st.success("✅ Book successfully added!")
                        # Optionally display the response JSON or message
                        with st.expander("View Server Response"):
                            st.json(response.json())
                    else:
                        st.error(f"❌ Failed to add book. Server returned status code: {response.status_code}")
                        st.write(response.text)
                        
                except requests.exceptions.RequestException as e:
                    st.error("❌ Connection error. Could not reach the API.")
                    st.exception(e)

if __name__ == "__main__":
    main()