const express = require("express")
const router = express.Router()
const bookController = require("../controllers/books")

router.post("/", bookController.saveBook)
router.get("/", bookController.getAllBook)
router.get("/:id", bookController.getOneBook)
router.put("/:id", bookController.modifyBook)
router.delete("/:id", bookController.deleteBook)

module.exports = router