import React from 'react';

const ProductBrowser = (props) => {
    const ui = useSelector(state => state.ui);
    const categories = useSelector(state => state.categories);
    const products = useSelector(state => state.products);
    let currentProducts = products.ids.map(id => products.dict[id]);

    useEffect(() => {
        if (ui.currentCategory) {
            // make an array of products that are part of the category
            currentProducts = products.ids.filter(id => categories.dict[ui.currentCategory].productIds.includes(id)).map()
        }
    }, [ui]);

    return (
        <>

        </>
    );
}

export default ProductBrowser;
