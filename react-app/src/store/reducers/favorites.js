import { TOGGLE_FAVORITE } from '../actions/favorites';

export default function reducer(state = [], action) {
    let newState = state;

    switch (action.type) {
        case TOGGLE_FAVORITE:
            if (newState.includes(action.productId)) {
                newState = newState.filter(el => el !== action.productId);
            } else {
                newState.push(action.productId);
            }
            return newState;
        default:
            return state;
    }
}
