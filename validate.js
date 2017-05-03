// JavaScript source code

function validate_fileupload() {
    //list allow of type
    var filesUpload = document.getElementById("filename[]");
    var errorMsg = document.getElementById("error");
    filesSize = filesUpload.files.length;
    if (filesSize < 2.0) {
        errorMsg.innerHTML = "Please upload two or more files";
        return false;
    } else {
        for (i = 0; i < filesUpload.files.length; i++) {
            if (filesUpload.files[i].name.split('.').pop().toLowerCase() !== "txt") {
                errorMsg.innerHTML = "Please upload txt file only";
                return false;
            }
        }
    }

    return true;
}
