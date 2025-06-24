const express = require("express")
const mongoose = require("mongoose")
require("dotenv").config()
const bookRouter = require("./routes/books")
const userRouter = require("./routes/user")
const app = express()

const MONGO_DB_URL = process.env.MONGO_DB_URL

mongoose.connect(MONGO_DB_URL)
    .then(() => console.log("Connexion à la base de donnée réussie !"))
    .catch((error) => console.log("Échec de la connexion à la base de donnée", error))

app.use(express.json())

app.use("/books", bookRouter)
app.use("/auth", userRouter)

app.use((req, res) => {
    res.status(404).json({message: "Route introuvable !"})
})

module.exports = app