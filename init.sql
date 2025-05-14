CREATE TABLE IF NOT EXISTS items (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    quantity INTEGER NOT NULL
);

INSERT INTO items (name, quantity) VALUES
('Apple', 10),
('Banana', 20);
