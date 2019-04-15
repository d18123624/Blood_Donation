/* eslint-disable */
export default {
    setIsLoggedIn(state, { loggedin, token }) {
        state.isloggedIn = loggedin;
        if (loggedin) {
            localStorage.setItem('token', token);
        } else {
            localStorage.removeItem('token');
        }
    }
}
