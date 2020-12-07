import { AUTHENTICATE_USER, LOGOUT_USER } from '../actions/auth';

export default reducer(state='', action) {
    let newState = { ...state };
    switch(action.type) {
        case AUTHENTICATE_USER:
            
        case LOGOUT_USER:

        default:
            return newState;
    }
}
