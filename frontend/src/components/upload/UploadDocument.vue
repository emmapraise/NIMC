<template>
	<div>
		<b-tabs content-class="mt-3 w-75 mx-auto" justified v-model="tabIndex">
			<b-tab title="Education" active>
				<education-vue />
			</b-tab>
			<b-tab title="CV">
				<cv-vue />
			</b-tab>
			<b-tab title="Professional Document">
				<professional-document-vue />
			</b-tab>
			<b-tab title="Certificates">
				<certificate-document-vue />
			</b-tab>
		</b-tabs>
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
		return {};
	},
};
</script>
