const Book = require("../model/Book")

exports.saveBook = (req, res, next) => {
    const book = new Book({
        ...req.body
    })
    book.save()
        .then(() => res.status(201).json({ message: "Livre enregistrée avec succès !" }))
        .catch(error => res.status(400).json({error}))
}

exports.getAllBook =  (req, res) => {
    Book.find()
        .then((books) => res.status(200).json(books))
        .catch(error => res.status(404).json({error}))
}

exports.getOneBook =  (req, res, next) => {
    Book.findOne({_id: req.params.id})
        .then((thisBook) => res.status(200).json(thisBook))
        .catch(error => res.status(404).json({error}))
}

exports.modifyBook =  (req, res, next) => {
    Book.findOneAndUpdate({ _id: req.params.id }, {...req.body, _id: req.params.id})
        .then(() => res.status(200).json({ message: "Livre modifiée avec succès !" }))
        .catch(error => res.status(400).json({error}))
}

exports.deleteBook =  (req, res, next) => {
    Book.findOneAndDelete({ _id: req.params.id })
        .then(() => res.status(200).json({ message: "Livre supprimé avec succès !" }))
        .catch(error => res.status(400).json({error}))
}
