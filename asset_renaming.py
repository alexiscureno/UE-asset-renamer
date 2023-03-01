import unreal


def rename_assets(search_pattern, replace_pattern, use_case):
    # unreal classes instances

    system_lib = unreal.SystemLibrary()
    edit_util = unreal.EditorUtilityLibrary()
    string_lib = unreal.StringLibrary()


    # get the selected assets and number for displaying

    selected_assets = edit_util.get_selected_assets()
    num_assets = len(selected_assets)
    replaced = 0

    unreal.log("Selected {} assets".format(num_assets))

    # this loops over each asset and renames it

    for asset in selected_assets:
        asset_name = system_lib.get_object_name(asset)

        # check if the asset name contains the given string and checks if its case-sensitive
        if string_lib.contains(asset_name, search_pattern, use_case=use_case):
            search_case = unreal.SearchCase.CASE_SENSITIVE if use_case else unreal.SearchCase.IGNORE_CASE
            replaced_name = string_lib.replace(asset_name, search_pattern, replace_pattern, search_case=search_case)
            edit_util.rename_asset(asset, replaced_name)

            replaced += 1
            unreal.log('Replaced {} with {}.'.format(asset_name, replaced_name))

        else:
            unreal.log("{} did not match the search pattern, was skipped".format(asset_name))

    unreal.log('replaced {} of {} assets'.format(replaced, num_assets))


rename_assets('New', 'Old', True)
