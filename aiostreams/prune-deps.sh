#!/bin/sh
set -eux

cd /app/node_modules/.pnpm
rm -rf \
    react* \
    @reduxjs+toolkit@* \
    @tanstack+table-core@* \
    @tanstack+react-table@* \
    @tanstack+react-virtual@* \
    @tanstack+virtual-core@* \
    victory-vendor@* \
    @hookform+resolvers@* \
    csstype@* \
    immer@* \
    zod@3.22.0 \
    @radix-ui+* \
    @floating-ui+* \
    d3-* \
    @types+d3-* \
    nano-css@* \
    css-in-js-utils@* \
    hyphenate-style-name@* \
    inline-style-prefixer@* \
    rtl-css-js@* \
    stylis@* \
    colord@* \
    scheduler@* \
    prop-types@* \
    loose-envify@* \
    use-sync-external-store@* \
    tiny-invariant@* \
    file-selector@* \
    attr-accept@* \
    copy-to-clipboard@* \
    toggle-selection@* \
    resize-observer-polyfill@* \
    screenfull@* \
    @xobotyi+scrollbar-width@* \
    ts-easing@* \
    decimal.js-light@*

echo "Dependency pruning complete."
