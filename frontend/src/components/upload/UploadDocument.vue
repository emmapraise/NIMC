<template>
	<div>
		<b-tabs
			content-class="mt-3 w-75 mx-auto"
			justified
			v-model="tabIndex"
			v-if="!isLoading"
		>
			<b-tab title="Education" active>
				<education-vue :citizens="results" />
			</b-tab>
			<b-tab title="CV">
				<cv-vue :citizens="results" />
			</b-tab>
			<b-tab title="Professional Document">
				<professional-document-vue :citizens="results" />
			</b-tab>
			<b-tab title="Certificates">
				<certificate-document-vue :citizens="results" />
			</b-tab>
		</b-tabs>
		<div v-else class="d-flex justify-content-center mb-3">
			<b-spinner
				type="grow"
				variant="info"
				style="width: 3rem; height: 3rem"
				label="loading"
			/>
		</div>
	</div>
</template>
<script>
import EducationVue from '../documents/Education.vue';
import CvVue from '../documents/Cv.vue';
import CertificateDocumentVue from '../documents/CertificateDocument.vue';
import ProfessionalDocumentVue from '../documents/ProfessionalDocument.vue';
export default {
	name: 'UploadDocumentComponent',
	components: {
		EducationVue,
		CvVue,
		ProfessionalDocumentVue,
		CertificateDocumentVue,
	},
	data() {
		return {
			results: [],
			isLoading: true,
			tabIndex: null,
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
