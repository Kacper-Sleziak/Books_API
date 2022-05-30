# Books_API

Application created as a recruitment task. The app is using a third-part google books API.

link : https://djangobooksapiproject.herokuapp.com

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
![Przechwytywanie](https://user-images.githubusercontent.com/57037642/170962160-c8df8520-33b6-43da-a962-3d6d5ffee724.PNG)
