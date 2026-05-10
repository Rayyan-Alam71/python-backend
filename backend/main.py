from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware  
app = FastAPI()

# Define your allowed origins (e.g., your frontend URL)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Or ["*"] to allow all origins (not recommended for production)
    allow_credentials=True,           # Allow cookies/authentication headers
    allow_methods=["*"],              # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],              # Allow all headers
)

posts : list[dict] =[
    {"id": 1, "title": "First Post", "content": "This is the content of the first post."},
    {"id": 2, "title": "Second Post", "content": "This is the content of the second post."},    
    {"id": 3, "title": "Third Post", "content": "This is the content of the third post."}
]


@app.get("/", include_in_schema=False)
@app.get("/posts", include_in_schema=False)
def read_root():
    html_content = """
    <html>
        <head>
            <title>My Blog</title>
        </head>
        <body>
            <h1>Welcome to My Blog</h1>
            <p>This is a simple blog application built with FastAPI.</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)


@app.get("/api/posts")
def read_posts():
    return posts
