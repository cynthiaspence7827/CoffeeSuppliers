export const TOGGLE_FAVORITE = 'TOGGLE_FAVORITE';

export const toggleFavoriteAction = productId => ({ type: TOGGLE_FAVORITE, productId });

export const toggleFavorite = (userId, productId) => async dispatch => {
    const data = await fetch(`/api/users/${userId}/favorites`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ productId })
    });
    if (data.ok) {
        const favorite = data.json();
        dispatch(toggleFavorite(productId))
    }
}
