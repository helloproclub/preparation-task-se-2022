const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const bookSchema = new Schema({
    title: {
        type: String,
        required: true
    },
    author: {
        type: String,
        required: true
    },
    year: {
        type: Number,
        required: true
    },
    category: {
        type: String,
        enum: ['Classic', 'Biography', 'Children', 'Fantasy', 'Horror', 'Romance', 'Science']
    },
    cover: {
        type: String,
        default: ""
    }
});

module.exports = mongoose.model('Book', bookSchema);
