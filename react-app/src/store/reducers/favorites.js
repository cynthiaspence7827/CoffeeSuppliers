

const initialState = {
    dict: {},
    ids: []
};

export default function reducer(state = initialState, action) {
    let newState = { ...state };

    switch (action.type) {

        default:
            return state;
    }
}
