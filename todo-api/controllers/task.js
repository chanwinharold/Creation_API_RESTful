const Task = require("../model/Task")

exports.createTask = (req, res, next) => {
    const task = new Task({
        ...req.body
    })
    task.save()
        .then(() => res.status(201).json({message: "Création de Tâche réussie"}))
        .catch(error => res.status(400).json({error}))
}

exports.getAllTask = (req, res, next) => {
    Task.find()
        .then((task) => res.status(200).json(task))
        .catch(error => res.status(404).json({error}))
}

exports.getOneTask = (req, res, next) => {
    Task.findById(req.params.id)
        .then((task) => res.status(200).json(task))
        .catch(error => res.status(404).json({error}))
}

exports.modifyTask = (req, res, next) => {
    Task.findByIdAndUpdate(req.params.id, req.body)
        .then(() => res.status(201).json({message: "Tâche modifiée avec succès"}))
        .catch(error => res.status(400).json({error}))
}

exports.deleteTask = (req, res) => {
    Task.findByIdAndDelete(req.params.id)
        .then(() => res.status(200).json({message: "Tâche supprimée avec succès"}))
        .catch(error => res.status(400).json({error}))
}