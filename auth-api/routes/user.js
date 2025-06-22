const express = require("express")
const router = express.Router()
const userControllers = require("../controllers/user")
const auth = require("../middlewares/auth")

router.post("/signup", userControllers.signup)
router.post("/login", userControllers.login)

router.get("/private", auth, (req, res, next) => {
    res.status(200).json( {message: "Requête reçu !"} )
})

module.exports = router