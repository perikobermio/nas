<template>
  <v-app>
     <v-main>
       <v-container class="grey-darken-1">
         <v-row class="justify-center">
           <v-col cols="12" class="text-center">
             <v-sheet color="blue-darken-2" class="py-2">
               <h1 class="white">Aurkibidea</h1>
             </v-sheet>
           </v-col>
         </v-row>

         <v-card color="blue-lighten-4" class="mb-8">
           <v-card-title color="blue-darken-2">Download Scripts</v-card-title>
           <v-card-text>
             <v-row>
				<v-col>
					<v-card class="white" flat>
						<v-card-title class="blue-darken-2">
							MEGADL
							<v-btn @click="mega_add"  class="mx-4" prepend-icon="mdi-plus" size="large" variant="outlined"> Gehitxu</v-btn>
							<v-btn @click="mega_save" prepend-icon="mdi-content-save" size="large" color="success"> Gorde</v-btn>
						</v-card-title>
				        <v-card-text>

				        	<v-sheet v-for="(item, index) in mega_urls" elevation="4" rounded class="mb-2">
				        		<v-card color="grey-lighten-2">
				        			<v-card-actions>
				        				<v-btn @click="mega_delete(index)" icon="mdi-delete" size="large" color="blue-darken-2"></v-btn>
				        			</v-card-actions>
				        			<v-card-text>
				        				<v-text-field v-model="item.url" label="Mega URL" required dense></v-text-field>
				        				<v-text-field v-model="item.download_path" label="Path" required dense></v-text-field>
				        			</v-card-text>
				        		</v-card>
				        	</v-sheet>
						
				        </v-card-text>
					</v-card>
				</v-col>
	          </v-row>
	     	</v-card-text>
	     </v-card>

         <v-row v-for="(item, index) in items" class="justify-center mb-5">
           <v-col cols="12">
             <v-card color="blue-lighten-4">
               <v-card-title>
                 <v-icon left color="blue" class="mr-4">mdi-{{item.icon}} </v-icon>
                 <a :href="item.link" target="_blank" class="blue-darken-4"> {{ item.title }}</a>
               </v-card-title>
               <v-card-text>
                 {{ item.description }}
               </v-card-text>
             </v-card>
           </v-col>
         </v-row>
         
       </v-container>
     </v-main>
   </v-app>
</template>

<script>
export default {
  name: 'master',
  data() {
	return {
	  items: [
	  	{ title: "Plex",icon: "plex", description: "PLEX server. Media center pertsonalizatue.", link: "http://plex.ebu.freemyip.com"},
	    { title: "Wireguard", icon: "key", description: "VPN. Chuwi makineko VPN pertsonala", link: "http://wireguard.ebu.freemyip.com"},
	    { title: "Pihole", icon: "advertisements", description: "ADS blocker. Ublock-elakue baie server mandan.", link: "http://pihole.ebu.freemyip.com/admin/"},
	    { title: "File browser", icon: "file-tree", description: "File browser karpeta konpartiduentzako. NAS osue konpartiten da.", link: "http://browser.ebu.freemyip.com"},
	  ],
	  mega_urls: []
	};
  },
  created() {
  	this.getMegaJson()
  },
  methods: {
  	getMegaJson() {
  		fetch('api/mega')
  			.then(r => r.json())
  			.then(data => {
  				this.mega_urls = data
  			})
  			.catch(e => {console.log(e)})
  	},
  	mega_delete(index) {
  		this.mega_urls.splice(index, 1)
  	},
  	mega_add() {
  		this.mega_urls.push({url: '', download_path: ''})
  	},
  	mega_save() {
  		fetch('api/mega', {
  				method: 'POST',
  				headers: {"Content-type": "Application/json"},
  				body: JSON.stringify(this.mega_urls)
  			})
  			.then(r => r.json())
  			.then(data => {
  				console.log(data)
  			})
  			.catch(e => {console.log(e)})
  	}
  }
}
</script>

<style scope>
html {
	background-color: red;
}

a {
	text-decoration: none;
	color: #1976d2;
}
</style>
