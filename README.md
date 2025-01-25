# Book Recommendation System

This is a book recommendation system built using Flask and machine learning techniques. The application provides personalized book recommendations based on a user-inputted book. It uses a content-based filtering approach to suggest similar books.

## Features
- **Book Recommendation**: Suggests books similar to the one the user inputs.
- **Popular Books Display**: Shows a list of popular books with ratings, authors, and cover images.
- **User Interface**: A simple web interface built using Flask for easy interaction.

## How It Works
- The user selects or inputs a book title.
- The system processes the input, finds similar books using precomputed similarity scores, and displays recommendations.

This system leverages pre-trained models stored in pickled files, optimizing speed and performance.
