// src/components/AddTodo.js
import React, { useState } from 'react';
import axios from 'axios';

const AddTodo = () => {
    const [projectName, setProjectName] = useState('');
    const [description, setDescription] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            await axios.post('http://localhost:8000/todo/apiitems/', {
                project_name: projectName,
                description: description,
                done: false,
                deadline: '2021-12-31',
                date: '2021-10-01',
            });
            setProjectName('');
            setDescription('');
            alert('Todo added successfully!');
        } catch (error) {
            console.error('Error adding todo: ', error);
            alert('Failed to add todo.');
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Project Name:
                <input
                    type="text"
                    value={projectName}
                    onChange={e => setProjectName(e.target.value)}
                    required
                />
            </label>
            <br />
            <label>
                Description:
                <input
                    type="text"
                    value={description}
                    onChange={e => setDescription(e.target.value)}
                    required
                />
            </label>
            <br />
            <button type="submit">Add Todo</button>
        </form>
    );
};

export default AddTodo;
