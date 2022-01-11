function deleteNote(noteId) {
    fetch("/delete-note", { // send a post request to the delete-note endpt. 
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/"; // this is used to refresh the page
    });
  }