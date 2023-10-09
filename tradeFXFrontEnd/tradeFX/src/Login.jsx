import React, { useState } from 'react';


const Login = () => {
    const [formData, setFormdata] = useState({username: '', password: ''});

    const handleInputChange = (e) => {
        const {name, value} = e.target;
        setFormdata({...formData, [name]: value});
    }
    const handleFormSubmit = async(e) => {
        e.preventDefault;
        url = 'http://127.0.0.1:8000/api/login/';

        const response = await fetch(url, {
            method: 'POST',
            headers: {
            'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });
        if (response.status === 200) {
            alert('Logged in successfully!');
        } else {
            alert('Login failed');
        }
    }
    return (
        <div>
            <h1>LOGIN</h1>
            <form onSubmit={handleFormSubmit}>
                <div>
                    <label>Username
                    <input type="text" name="username" id="username" value={formData.username} onChange={handleInputChange} />
                    </label>
                </div>
                <div>
                    <label>Password
                    <input type="password" name="password" id="password" value={formData.password} onChange={handleInputChange} />
                    </label>
                </div>
                <button type="submit">Login</button>
            </form>
        </div>
    )
}

export default Login;