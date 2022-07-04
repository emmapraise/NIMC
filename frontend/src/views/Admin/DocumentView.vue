<template>
	<div>
		<header-vue :logout="true" />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card title="Upload Document" class="">
					<b-form
						@submit.prevent="onSubmit"
						validated="true"
						class="was-validated"
						v-if="!isLoading"
					>
						<b-form-input list="citizen-list" v-model="result"></b-form-input>
						<datalist id="citizen-list">
							<option v-for="(item, index) in results" :key="index">
								{{ item.user.first_name }} {{ item.user.last_name }} (
								{{ item.user.nin }})
							</option>
						</datalist>
						<upload-document-vue />
					</b-form>
				</b-card>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '../../components/header/Header.vue';
import SidebarVue from '../../components/sidebar/Sidebar.vue';
import UploadDocumentVue from '../../components/upload/UploadDocument.vue';
export default {
	name: 'UploadDocument',
	components: {
		HeaderVue,
		SidebarVue,
		UploadDocumentVue,
	},
	data() {
		return {
			results: [],
			isLoading: true,
			result: '',
		};
	},
	created() {
		this.getCitizen();
	},
	methods: {
		async getCitizen() {
			await this.axios
				.get(`api/citizen/`)
				.then(({ data }) => {
					console.log(data.results);
					this.results = data.results;
					this.isLoading = false;
				})
				.catch((err) => {
					console.log(err);
				});
		},
	},
};
</script>
