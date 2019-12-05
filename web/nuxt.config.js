import pkg from './package';

const flaskApiUrl = 'http://127.0.0.1:5000/';
export default {
    mode: 'spa',

    /*
     ** Headers of the page
     */
    head: {
        title: pkg.name,
        meta: [
            { charset: 'utf-8' },
            {
                name: 'viewport',
                content: 'width=device-width, initial-scale=1',
            },
            {
                hid: 'description',
                name: 'description',
                content: pkg.description,
            },
        ],
        link: [
            { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
            {
                rel: 'stylesheet',
                href:
                    'https://fonts.googleapis.com/css?family=Lato|Montserrat|Roboto&display=swap',
            },
        ],
    },

    /*
     ** Customize the progress-bar color
     */
    loading: { color: '#fff' },

    /*
     ** Global CSS
     */
    css: [
        'element-ui/lib/theme-chalk/index.css',
        // Load a Node.js module directly (here it's a Sass file)
        'bulma/css/bulma.css',
        // // CSS file in the project
        // // '@/assets/css/main.css',
        // SCSS file in the project
        '~/scss/main.scss',
    ],
    render: {
        bundleRenderer: {
            shouldPreload: (file, type) => {
                return ['script', 'style', 'font'].includes(type);
            },
        },
    },

    /*
     ** Plugins to load before mounting the App
     */
    plugins: ['@/plugins/element-ui'],

    /*
     ** Nuxt.js modules
     */
    modules: ['@nuxtjs/style-resources', '@nuxtjs/axios', '@nuxtjs/proxy'],
    styleResources: {
        scss: ['~scss/main.scss'],
    },

    axios: {
        baseURL: flaskApiUrl,
        prefix: '/api',
        proxy: true,
    },

    /**
     * Proxy module settings
     */
    proxy: {
        '/api': {
            target: flaskApiUrl,
            ws: false,
            pathRewrite: { '^/api/': '' },
        },
    },
    /*
     ** Build configuration
     */
    build: {
        transpile: [/^element-ui/],
        // postcss: {
        //     plugins: {
        //         'postcss-preset-env': {
        //             features: {
        //                 customProperties: false,
        //             },
        //         },
        //     },
        // },

        /*
         ** You can extend webpack config here
         */
        extend(config, ctx) {
            // Run ESLint on save
            // if (ctx.isDev && ctx.isClient) {
            //     config.module.rules.push({
            //         enforce: 'pre',
            //         test: /\.(js|vue)$/,
            //         loader: 'eslint-loader',
            //         exclude: /(node_modules)/,
            //     });
            // }
        },
    },
};
