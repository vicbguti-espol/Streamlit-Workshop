import streamlit as st

class WebApp:
    def page_first(self):
        st.title("This is my first page")
        # ...


    def page_second(self):
        st.title("This is my second page")
        # ...

def main():
    app = WebApp()
    # Register your pages
    pages = {
        "First page": app.page_first,
        "Second page": app.page_second,
    }

    st.sidebar.title("App with pages")

    # Widget to select your page, you can choose between radio buttons or a selectbox
    page = st.sidebar.selectbox("Select your page", tuple(pages.keys()))
    #page = st.sidebar.radio("Select your page", tuple(pages.keys()))

    # Display the selected page with the session state
    pages[page]()





if __name__ == "__main__":
    main()