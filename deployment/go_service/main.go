package main

import (
	"net/http"
	"github.com/gorilla/csrf"
	"github.com/gorilla/mux"
)

func main() {
	r := mux.NewRouter()
	csrfMiddleware := csrf.Protect([]byte("32-byte-long-auth-key"))

	r.HandleFunc("/submit", SubmitHandler)
	http.ListenAndServe(":8000", csrfMiddleware(r))
}

func SubmitHandler(w http.ResponseWriter, r *http.Request) {
	http.SetCookie(w, &http.Cookie{
		Name:     "session_id",
		Value:    "your-session-id",
		HttpOnly: true,
		SameSite: http.SameSiteLaxMode,
	})
	// Handle form submission
} 