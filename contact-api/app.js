const express = require("express")
const mongoose = require("mongoose")
const contactRouter = require("./routes/contact")
const userRouter = require("./routes/user")
const app = express()
require("dotenv").config()

mongoose.connect(process.env.MONDO_DB_URL)
    .then(() => console.log("Connexion à MongoDB réussie"))
    .catch(error => console.log("Échec de la connexion à MongoDB", error))

app.use(express.json())

app.use('/contacts', contactRouter)
app.use('/auth', userRouter)

app.use((req, res, next) => {
    res.status(400).json({ message: "Route Introuvable !" })
})

module.exports = app