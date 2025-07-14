const Contact = require("../models/Contact")


exports.createContact = (req, res, next) => {
    delete req.body._id
    delete req.body.userId

    const contact = new Contact({
        ...req.body,
        userId : req.auth.userId
    })
    contact.save()
        .then(() => res.status(201).json({ message: "Contact enregistré !" }))
        .catch(error => res.status(401).json({ error }))
}

exports.getAllContact = (req, res, next) => {
    Contact.find({ userId: req.auth.userId })
        .then((contacts) => res.status(200).json({ contacts }))
        .catch(error => res.status(401).json({ error }))
}

exports.getOneContact = (req, res, next) => {
    Contact.findOne({ userId: req.auth.userId, _id: req.params.id })
        .then((contact) => res.status(200).json({ contact }))
        .catch(error => res.status(401).json({ error }))
}

exports.modifyContact = (req, res, next) => {
    Contact.findOneAndUpdate({ userId : req.auth.userId, _id: req.params.id }, { ...req.body, _id: req.params.id } )
        .then(() => res.status(201).json({ message: "Contact modifié !" }))
        .catch(error => res.status(401).json({ error }))
}

exports.deleteContact = (req, res, next) => {
    Contact.findOneAndDelete({ userId : req.auth.userId, _id: req.params.id } )
        .then(() => res.status(201).json({ message: "Contact supprimé !" }))
        .catch(error => res.status(401).json({ error }))
}