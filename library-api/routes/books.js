const express = require("express")
const router = express.Router()
const bookController = require("../controllers/books")
const auth = require("../middlewares/auth")

router.post("/", auth, bookController.saveBook)
router.get("/", auth, bookController.getAllBook)
router.get("/:id", auth, bookController.getOneBook)
router.put("/:id", auth, bookController.modifyBook)
router.delete("/:id", auth, bookController.deleteBook)

module.exports = router