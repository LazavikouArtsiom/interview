import React from "react";

import styles from "./Catalog.module.css";
import CatalogItem from "./CatalogItem/CatalogItem";
import Filter from "./Filter/Filter";
import Pagination from "./Pagination/Pagination";

const Catalog = () => {
  return (
    <div className={styles.catalog}>
      <Filter />
      <div className={styles.right}>
        <div className={styles.catalogItems}>
          <CatalogItem />
          <CatalogItem />
          <CatalogItem />
        </div>
        <Pagination />
      </div>
    </div>
  );
};

export default Catalog;
