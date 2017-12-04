ventazApp
//------------------------------
// TODO: API menu
// por lo pronto colocar aqui el menu para su Modelo, vease test1
//------------------------------
.factory("menuService", [
  '$location',
  '$rootScope',
  '$http',
  '$window',
  function($location, $rootScope, $http, $window) {

    var version = {};

    var sections = [
    {
      name: 'Inicio',
      state: 'Inicio',
      url: '/Inicio',
      type: 'link'
    }

    ];
    /*
    var sections = [
    {
      name: 'Getting Started',
      state: 'getting-started',
      url: '/getting-started',
      type: 'link'
    }

    ];
    */
    sections.push({
        name: 'EMPRESA',
        type: 'toggle',
        pages: [
        {
          name : 'ALMACEN',
          state: 'Almacen',
          url: '/Almacen',
          type: 'link'
        },
        {
          name : 'ESTABLECIMIENTO/NOGOCIO',
          state: 'EstablecimientoNegocio',
          url: '/EstablecimientoNegocio',
          type: 'link'
        }
        ]
    });
    sections.push({
        name: 'RRHH',
        type: 'toggle',
        pages: [
        {
          name : 'CLIENTES',
          state: 'Cliente',
          url: '/Cliente',
          type: 'link'
        },
        {
          name : 'TRABAJADORES',
          state: 'Trabajador',
          url: '/Trabajador',
          type: 'link'
        },
        {
          name : 'PROVEEDORES',
          state: 'Proveedor',
          url: '/Proveedor',
          type: 'link'
        }
        ]
    });
    sections.push({
        name: 'INSUMOS',
        type: 'toggle',
        pages: [
        {
          name : 'CATEGORIAS',
          state: 'Categoria',
          url: '/Categoria',
          type: 'link'
        },
        {
          name : 'PRODUCTOS',
          state: 'Producto',
          url: '/Producto',
          type: 'link'
        }
        ]
    });
    sections.push({
        name: 'ACCIONES',
        type: 'toggle',
        pages: [
        {
          name : 'VENTAS',
          state: 'Venta',
          url: '/Venta',
          type: 'link'
        },
        {
          name : 'COMPRAS',
          state: 'Compras',
          url: '/Compras',
          type: 'link'
        }
        
        ]
    });

    function sortByName(a,b) {
      return a.name < b.name ? -1 : 1;
    }

    var self;

    $rootScope.$on('$locationChangeSuccess', onLocationChange);



    return self = {
      version   :  version,
      sections  : sections,

      selectSection: function(section) {
        self.openedSection = section;
      },
      toggleSelectSection: function(section) {
        self.openedSection = (self.openedSection === section ? null : section);
      },
      isSectionSelected: function(section) {
        return self.openedSection === section;
      },

      selectPage: function(section, page) {
        self.currentSection = section;
        self.currentPage = page;
      },
      isPageSelected: function(page) {
        return self.currentPage === page;
      }
    };

    function sortByHumanName(a,b) {
      return (a.humanName < b.humanName) ? -1 :
      (a.humanName > b.humanName) ? 1 : 0;
    }

    function onLocationChange() {
      var path = $location.path();
      var introLink = {
        name: "SISTEMA",
        //name: "Introduction",
        url:  "/",
        type: "link"
      };

      if (path == '/') {
        self.selectSection(introLink);
        self.selectPage(introLink, introLink);
        return;
      }

      var matchPage = function(section, page) {
        if (path === page.url) {
          self.selectSection(section);
          self.selectPage(section, page);
        }
      };

      sections.forEach(function(section) {
        if(section.children) {
        // matches nested section toggles, such as API or Customization
        section.children.forEach(function(childSection){
          if(childSection.pages){
            childSection.pages.forEach(function(page){
              matchPage(childSection, page);
            });
          }
        });
      }
      else if(section.pages) {
        // matches top-level section toggles, such as Demos
        section.pages.forEach(function(page) {
          matchPage(section, page);
        });
      }
      else if (section.type === 'link') {
        // matches top-level links, such as "Getting Started"
        matchPage(section, section);
      }
    });
    }
  }]);