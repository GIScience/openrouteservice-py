import { defineConfig } from 'vitepress'
import defineVersionedConfig from 'vitepress-versioning-plugin';

// https://vitepress.dev/reference/site-config
export default defineVersionedConfig(__dirname, {
  ignoreDeadLinks: true,
  title: "openrouteservice-py",
  description: "🐍 The Python API to consume openrouteservice(s) painlessly! ",
  base: '/openrouteservice-py/',
  head: [
    ['link', { rel: "icon", type: "image/png", sizes: "32x32", href: "https://giscience.github.io/openrouteservice/ors_fav.png"}],
  ],
  markdown: {
    anchor: {
      slugify: (s) => encodeURIComponent(String(s).trim().toLowerCase().replace(/\s+/g, '_'))
    },
  },
  vite: {
    publicDir: "./examples"
  },
  themeConfig: {
    search: {
      provider: 'local'
    },
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Getting started', link: '/README' },
      { text: 'Forum', link: 'https://ask.openrouteservice.org/c/sdks/10' },
      { text: 'API Playground', link: 'https://openrouteservice.org/dev/#/api-docs' }
    ],

    sidebar: [
      {
        text: 'Documentation',
        link: 'README#documentation-for-api-endpoints',
        items: [
          { text: 'Directions GeoJSON', link: '/docs/DirectionsServiceApi#get_geo_json_route' },
          { text: 'Directions JSON', link: '/docs/DirectionsServiceApi#get_json_route' },
          { text: 'Elevation Line', link: '/docs/ElevationApi#elevation_line_post' },
          { text: 'Elevation Point', link: '/docs/ElevationApi#elevation_point_post' },
          { text: 'Geocode Autocomplete ', link: '/docs/GeocodeApi#geocode_autocomplete_get' },
          { text: 'Reverse Geocode', link: '/docs/GeocodeApi#geocode_reverse_get' },
          { text: 'Forward Geocode', link: '/docs/GeocodeApi#geocode_search_get' },
          { text: 'Structured Forward Geocode', link: '/docs/GeocodeApi#geocode_search_structured_get' },
          { text: 'Isochrones', link: '/docs/IsochronesServiceApi#get_default_isochrones'},
          { text: 'Matrix', link: '/docs/MatrixServiceApi#get_default' },
          { text: 'Optimization', link: '/docs/OptimizationApi#optimization_post' },
          { text: 'POIs', link: '/docs/PoisApi#pois_post' }
        ]
      },
      {
        text: 'Examples',
        items: [
          { text: 'Avoid construction sites dynamically', link: 'docs/examples/Avoid_ConstructionSites' },
          { text: 'Dieselgate Routing', link: 'docs/examples/Dieselgate_Routing' },
          { text: 'Route optimization of pub crawl', link: 'docs/examples/ortools_pubcrawl' },
          { text: 'Routing optimization in humanitarian context', link: 'docs/examples/Routing_Optimization_Idai' }
        ]
      },
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/GIScience/openrouteservice-py' },
      { icon: 'x', link: 'https://twitter.com/ors_news' }
    ]
  },
  versioning: {
    latestVersion: "7.1.0.post6",
    switcher: {
      includeLatestVersion: true,
    },
  },
})
