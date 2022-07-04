<template>
	<div>
		<b-row v-for="(item, index) in cv_tab" :key="index" class="my-2">
			<b-col sm="3">
				<label :for="item.label">{{ item.name }}</label>
			</b-col>
			<b-col sm="9">
				<div v-if="item.type === 'combobox'">
					<user-combobox-vue :citizens="citizens" />
				</div>
				<div v-else>
					<b-form-file
						v-model="item.value"
						:state="Boolean(item.value)"
						placeholder="Choose a file or drop it here..."
						drop-placeholder="Drop file here..."
					></b-form-file>
				</div>
			</b-col>
		</b-row>
		<div class="float-right mt-3">
			<b-button variant="success">Submit</b-button>
		</div>
	</div>
</template>
<script>
import UserComboboxVue from '../combobox/UserCombobox.vue';
export default {
	name: 'CVComponent',
	components: { UserComboboxVue },
	props: ['citizens'],
	data() {
		return {
			cv_tab: [
				{
					name: 'User',
					label: 'citizen',
					type: 'combobox',
					value: '',
				},
				{
					name: 'Upload CV',
					label: 'upload_cv',
					type: 'file',
					value: null,
				},
			],
		};
	},
};
</script>
