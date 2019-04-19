/* eslint-disable */
export default {
    setIsLoggedIn(state, { loggedin, token }) {
        state.isloggedIn = loggedin;
        if (loggedin) {
            localStorage.setItem('token', token);
        } else {
            localStorage.removeItem('token');
        }
    },
    setSearchMarkers(state, { newPoints }) {
        state.searchMarkers = newPoints;
    },
    setIsIncomingRequestsOpen(state, data) {
        state.isIncomingRequestsOpen = data;
    },
    setMapCenter(state, { mapCenter }) {
        state.mapCenter = mapCenter;
    }
}
