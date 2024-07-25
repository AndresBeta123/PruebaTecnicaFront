<template>
  <div>
    <nav>
      <button @click="currentView = 'search'">Buscar Todos</button>
      <button @click="currentView = 'SearchByName'">Buscar Usuario </button>
      <button @click="currentView = 'SearchByID'">Mostrar suario por id</button>
      <button @click="currentView = 'Create'">Crear</button>
      <button @click="currentView = 'update'">Actualizar</button>
      <button @click="currentView = 'delete'">Eliminar</button>
      
      
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
  display: flex;
  gap: 10px;
  margin-bottom: 20px;
}
button {
  padding: 10px 20px;
  cursor: pointer;
}
</style>