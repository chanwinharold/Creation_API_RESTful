const Book = require("../model/Book")

exports.saveBook = (req, res, next) => {
    delete req.body._id
    delete req.body.userId
    const book = new Book({
        ...req.body,
        userId: req.auth.userId
    })
    book.save()
        .then(() => res.status(201).json({ message: "Livre enregistrée avec succès !" }))
        .catch(error => res.status(400).json({ error }))
}

exports.getAllBook =  (req, res, next) => {
    Book.find({ userId: req.auth.userId })
        .then((books) => res.status(200).json({ books }))
        .catch(error => res.status(404).json({ error }))
}

exports.getOneBook =  (req, res, next) => {
    Book.findOne({ _id: req.params.id, userId: req.auth.userId })
        .then((thisBook) => {
            if (!thisBook) {
                return res.status(404).json({ message: "Livre introuvable ou non-autorisé !" })
            }
            res.status(200).json({ thisBook })
        })
        .catch(error => res.status(404).json({ error }))
}

exports.modifyBook =  (req, res, next) => {
    Book.findOne({ _id: req.params.id, userId: req.auth.userId })
        .then(() => {
            Book.updateOne({ _id: req.params.id }, { ...req.books, _id: req.params.id, userId: req.auth.userId })
                .then(() => res.status(200).json({ message: "Livre modifié !" }))
                .catch(error => res.status(400).json({ error }))
        })
        .catch(error => res.status(404).json({ error }))
}

exports.deleteBook =  (req, res, next) => {
    Book.findOne({ _id: req.params.id, userId: req.auth.userId })
        .then(() => {
            Book.deleteOne({ _id: req.params.id, userId: req.auth.userId })
                .then(() => res.status(200).json({ message: "Livre supprimé avec succès !" }))
                .catch(error => res.status(404).json({ error }))
        })
        .catch(error => res.status(404).json({ error }))
}
