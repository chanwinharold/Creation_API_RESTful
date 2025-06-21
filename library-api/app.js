const express = require("express")
const app = express()
const mongoose = require("mongoose")
const bookRouter = require("./routes/books")

mongoose.connect("mongodb+srv://<user>:<password>@cluster0.44esyvl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    .then(() => console.log("Connexion à la base de donnée réussie !"))
    .catch((error) => console.log("Échec de la connexion à la base de donnée", error))

app.use(express.json())

app.use("/books", bookRouter)

app.use((req, res) => {
    res.status(404).json({message: "Route introuvable !"})
})

module.exports = app