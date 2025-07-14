const User = require("../models/User")
const bcrypt = require("bcrypt")
const jwt = require("jsonwebtoken")
require("dotenv").config()

exports.signup = (req, res, next) => {
    bcrypt.hash(req.body.password, 10)
        .then(hash => {
            const user = new User({
                username : req.body.username,
                password: hash
            })
            user.save()
                .then(() => res.status(201).json({ message: "Utilisateur enregistrée !" }))
                .catch(error => res.status(401).json({ error }))
        })
        .catch(error => res.status(500).json({ error }))
}

exports.login = (req, res, next) => {
    User.findOne({ username: req.body.username })
        .then(user => {
            if (!user) res.status(400).json({ message: "Username ou mot de passe incorrecte !" })
            else {
                bcrypt.compare(req.body.password, user.password)
                    .then(valid => {
                        if (!valid) res.status(400).json({ message: "Username ou mot de passe incorrecte !" })
                        else {
                            res.status(200).json({
                                userId : user._id,
                                token : jwt.sign(
                                {userId : user._id},
                                    process.env.JWT_KEY_SECRET,
                                    {expiresIn: '24h'}
                                )
                            })
                        }
                    })
                    .catch(error => res.status(500).json({ error }))
            }
        })
        .catch(error => res.status(500).json({ error }))
}