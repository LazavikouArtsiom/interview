import React from "react";

import styles from "./Pagination.module.css";
import PaginationItem from "./PaginationItem/PaginationItem";

const Pagination = () => {
    return (
        <div className={styles.pagination}>
            <PaginationItem />
            <PaginationItem />
            <PaginationItem />
            <PaginationItem />
            <PaginationItem />
        </div>
    );
};

export default Pagination;
