import React, { useState } from 'react';

const ToDoList = () => {
    const [todos, setTodos] = useState([]);
    const [newTodo, setNewTodo] = useState('');

    const handleAddTodo = () => {
        if (newTodo.trim() !== '') {
            setTodos([...todos, newTodo]);
            setNewTodo('');
        }
    };

    const handleDeleteTodo = (index) => {
        setTodos(todos.filter((_, i) => i !== index));
    };

    return (
        <div className="container">
            <h1>To-Do List</h1>
            <div className="todo-list">
                {todos.map((todo, index) => (
                    <div className="todo-item" key={index}>
                        <h3>{todo}</h3>
                        <button onClick={() => handleDeleteTodo(index)}>Delete</button>
                    </div>
                ))}
            </div>
            <div className="add-todo">
                <input
                    type="text"
                    placeholder="Enter new ToDo"
                    value={newTodo}
                    onChange={(e) => setNewTodo(e.target.value)}
                />
                <button onClick={handleAddTodo}>Add</button>
            </div>
        </div>
    );
};

export default ToDoList;
