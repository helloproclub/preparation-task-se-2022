const Book = require('../src/models/book');

const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/booku', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
});

const db = mongoose.connection;
db.on('error', console.error.bind(console, 'connection error:'));
db.once('open', () => {
    console.log("Database connected!")
})

const seedDB = async () => {
    // Remove all books before seeding
    await Book.deleteMany({});
    const books = [
        {
            title: "The Lord of the Rings",
            author: "J.R.R. Tolkien",
            year: 1954,
            category: "Fantasy",
        },
        {
            title: "The Hobbit",
            author: "J.R.R. Tolkien",
            year: 1937,
            category: "Fantasy",
        },
        {
            title: "The Catcher in the Rye",
            author: "J.D. Salinger",
            year: 1951,
            category: "Biography",
        },
        {
            title: "The Giver",
            author: "Lois Lowry",
            year: 1993,
            category: "Children",
        },
        {
            title: "The Hunger Games",
            author: "Suzanne Collins",
            year: 2008,
            category: "Science",
        },
        {
            title: "The Fault in Our Stars",
            author: "John Green",
            year: 2012,
            category: "Romance",
        },
        {
            title: "The Da Vinci Code",
            author: "Dan Brown",
            year: 2003,
            category: "Science",
        },
        {
            title: "The Alchemist",
            author: "Paulo Coelho",
            year: 1988,
            category: "Romance",
        },
    ];

    for (book of books) {
        const newBook = new Book(book);
        await newBook.save();
    }

    console.log("Database seeded!")
    mongoose.connection.close();
}

seedDB();
