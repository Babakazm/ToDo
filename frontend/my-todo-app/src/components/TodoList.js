// src/components/TodoList.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const TodoList = () => {
    const [todos, setTodos] = useState([]);

    useEffect(() => {
        const fetchTodos = async () => {
            try {
                const response = await axios.get('http://localhost:8000/todo/apiitems');
                setTodos(response.data);
            } catch (error) {
                console.error('Error fetching data: ', error);
            }
        };

        fetchTodos();
    }, []);

    return (
        <ul>
            {todos.map(todo => (
                <table>
                    <tr key={todo.id}></tr>
                    <tr>{todo.project_name}</tr>                    
                        <li key={todo.id}>{todo.project_name} - {todo.description}</li>
                </table>
            ))}
        </ul>
    );
};

export default TodoList;
