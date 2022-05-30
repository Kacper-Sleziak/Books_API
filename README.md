# Books_API

Application created as a recruitment task. The app is using a third-part google books API.

## API 
### GET/api_spec

### GET/books
- return books for given params (title, authors[], from, to, acquired), return all books for zero parameters

### POST/books/create
- create book for given in body parameters 

### GET/books/{pk}
- return book with given id 

### PUT/books/{pk}
- edit book with given id

### DELETE/books/{pk}
- delete book with given id

### POST/import
- import all books for given in body author from google API
