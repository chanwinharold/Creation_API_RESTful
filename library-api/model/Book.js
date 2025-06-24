const mongoose = require("mongoose")

const bookSchema = new mongoose.Schema({
    title: { type: String, required: true, unique: true },
    author: { type: String, required: true },
    year: { type: Number, required: true },
    userId: { type: String, required: true }
})

module.exports = mongoose.model("Book", bookSchema)