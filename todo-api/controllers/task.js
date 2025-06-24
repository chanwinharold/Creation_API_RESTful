const Task = require("../model/Task")

exports.createTask = (req, res, next) => {
    delete req.body._id
    delete req.body.userId
    const task = new Task({
        ...req.body,
        userId: req.auth.userId
    })
    task.save()
        .then(() => res.status(200).json({message: "Objet enregistré !"}))
        .catch(error => res.status(400).json( {error} ))
}

exports.getAllTask = (req, res, next) => {
    Task.find({userId: req.auth.userId})
        .then((tasks) => res.status(200).json(tasks))
        .catch(error => res.status(404).json({error}))
}

exports.getOneTask = (req, res, next) => {
    Task.findOne({_id: req.params.id, userId: req.auth.userId})
        .then((task) => {
            if (!task) {
                return res.status(404).json({message: "Tâche introuvable ou non autorisée"});
            }
            res.status(200).json(task)
        })
        .catch(error => res.status(404).json({error}))
}

exports.modifyTask = (req, res, next) => {
    Task.findById(req.params.id)
        .then(task => {
            if (task.userId !== req.auth.userId) {
                res.status(401).json({message: "Non-autorisée !"})
            } else {
                delete req.body.userId
                Task.updateOne({_id: req.params.id}, {...req.body, userId: req.auth.userId})
                    .then(() => res.status(200).json({message: "Objet modifié !"}))
                    .catch(error => res.status(400).json({error}))
            }
        })
        .catch(error => res.status(400).json({error}))
}

exports.deleteTask = (req, res) => {
    Task.findOne({_id: req.params.id})
        .then(task => {
            if (task.userId !== req.auth.userId) {
                res.status(401).json({message: "Non-autorisée !"})
            } else {
                Task.deleteOne({_id: req.params.id})
                    .then(() => res.status(200).json({message: "Objet supprimé !"}))
                    .catch(error => res.status(400).json({error}))
            }
        })
        .catch(error => res.status(400).json({error}))
}