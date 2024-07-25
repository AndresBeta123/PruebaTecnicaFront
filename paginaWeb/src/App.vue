  <template Class="center">
    <div>
      <nav class="navbar navbar-light bg-light">
        <form class="container-fluid justify-content-center">
          <button class="btn btn-outline-success me-2 btn-sm" type="button" @click="currentView = 'search'">Buscar Todos</button>
          <button class="btn btn-outline-success me-2 btn-sm" type="button" @click="currentView = 'SearchByName'">Buscar Usuario</button>
          <button class="btn btn-outline-success me-2 btn-sm" type="button" @click="currentView = 'SearchByID'">Mostrar usuario por ID</button>
          <button class="btn btn-outline-success me-2 btn-sm" type="button" @click="currentView = 'Create'">Crear</button>
          <button class="btn btn-outline-success me-2 btn-sm" type="button" @click="currentView = 'update'">Actualizar</button>
          <button class="btn btn-outline-success me-2 btn-sm" type="button" @click="currentView = 'delete'">Eliminar</button>
        </form>
      </nav>
      <component :is="currentViewComponent"></component>
    </div>
  </template>

  <script>
  import SearchForm from './components/SearchForm.vue';
  import SearchByName from './components/SearchByName.vue';
  import SearchByID from './components/SearchByID.vue';
  import DeleteForm from './components/DeleteForm.vue';
  import UpdateForm from './components/UpdateForm.vue';
  import CreateForm from './components/CreateForm.vue';

  export default {
    data() {
      return {
        currentView: 'search'
      };
    },
    computed: {
      currentViewComponent() {
        switch (this.currentView) {
          case 'search':
            return SearchForm;
          case 'SearchByName':
            return SearchByName;
          case 'SearchByID':
            return SearchByID;
          case 'delete':
            return DeleteForm;
          case 'update':
            return UpdateForm;
          case 'Create':
            return CreateForm;
          default:
            return SearchForm;
        }
      }
    }
  };
  </script>

  <style>
  nav {
    margin-bottom: 20px;
  }

  form {
    display: flex;
    flex-wrap: wrap;
    justify-content: right;
    gap: 10px;
  }

  button {
    padding: 10px 20px;
    cursor: pointer;
  }
  #app {
  display: flex;
  flex-direction: column;
  align-items: center; /* Centra el contenido horizontalmente */
  justify-content: center; /* Centra el contenido verticalmente si es necesario */
  min-height: 100vh; /* Asegura que el contenedor tenga al menos la altura de la ventana */
  padding: 0 2rem; /* Opcional: agrega algo de padding para los lados */
}

  </style>
