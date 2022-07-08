<template>
	<div>
		<header-vue :logout="true" />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card title="Upload Document" class="">
					<upload-document-vue />
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
			result: '',
		};
	},
	created() {},
	methods: {},
};
</script>
