const Register = () => {
    const fetchData = async () => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/trade/');
            if (response.status === 200) {
                const data = await response.json();
                console.log(data);
            } else {
                console.error('Failed to fetch traders');
            }
        } catch(err) {
            console.log('Error: ', err);
        }
    }
    // fetchData();
    return (
        <h1>Register</h1>
    )
}

export default Register;